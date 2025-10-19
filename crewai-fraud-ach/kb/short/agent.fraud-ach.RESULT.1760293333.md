```json
{
  "id": "f538f1c78299ff2c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293333,
  "host_pid": "9e6742732c60:1",
  "hash": "28b0b3490340be74b6c91b6a783b6436806875248f0f1d98c62a30cb2f6f1809",
  "cid": "QmV128b0b3490340be74b6c91b6a783b643680687524",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293333,
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
      "evaluated_at": 1760293333
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
  "sig": "ff06b8ac3f749330c9c33544ad49fd99e9230cd93c3484bc06d03ec90264a13c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241250323
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 216, 'threshold': 50, 'total_amount': 21382488, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 215, 'first_seen': 1760285763, 'matching_hash': 'd18939bbbb7c2a14'}}}