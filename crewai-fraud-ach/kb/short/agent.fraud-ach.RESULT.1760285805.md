```json
{
  "id": "978f421d64003ab0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285805,
  "host_pid": "9e6742732c60:1",
  "hash": "64aa89757638389db517630ef6dcba65e785e19996a2fca86784485fe657e35e",
  "cid": "QmV164aa89757638389db517630ef6dcba65e785e199",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285805,
      "method": "automated_fraud_detection",
      "vc_type": "VerifiableCredential"
    },
    "ucon": {
      "usage_constraints": [
        "no_pii_export",
        "audit_required"
      ],
      "purpose": "fraud_detection_analysis",
      "enforcement": "mandatory"
    },
    "eval": {
      "confidence": 1.0,
      "evidence_count": 0,
      "review_status": "pending",
      "evaluated_at": 1760285805
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "90f6d797821b73bf044911afc31b22cc8a13fa72b480c0b5b173aa70dc798044"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000245329334
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 2, 'first_seen': 1760285765, 'matching_hash': 'de3fbc58a94e529a'}}}