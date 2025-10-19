```json
{
  "id": "f12d16fbbfc3eff1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286642,
  "host_pid": "9e6742732c60:1",
  "hash": "d4a92e384234ed133c670d4a89db48df534297042ed30cf3f53ebb5fe122076e",
  "cid": "QmV1d4a92e384234ed133c670d4a89db48df53429704",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286642,
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
      "evaluated_at": 1760286642
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "0e9d23e14cb2d658e74a2e25a000be24034a83ac745b4d26d9fbbb5b0e8da722"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 021000021395098
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 11546432, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 31, 'first_seen': 1760285765, 'matching_hash': '9c6ceec1730a6176'}}}