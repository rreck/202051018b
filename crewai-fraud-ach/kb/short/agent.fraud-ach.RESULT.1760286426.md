```json
{
  "id": "1873647ba3346fc2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286426,
  "host_pid": "9e6742732c60:1",
  "hash": "e1ab5de4a3c973e5001c4982934ae1fed746248d757768783d294c42cb0962d0",
  "cid": "QmV1e1ab5de4a3c973e5001c4982934ae1fed746248d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286426,
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
      "evaluated_at": 1760286426
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
  "sig": "20e6bfacd75352adee338afd154d08224c64d6b0e022390b8ba116899f1a6335"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 026009592795708
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 11491275, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 24, 'first_seen': 1760285763, 'matching_hash': '6f9672c314113419'}}}