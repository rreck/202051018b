```json
{
  "id": "60f2b33dbc7860de",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287290,
  "host_pid": "9e6742732c60:1",
  "hash": "ee208ea41e17b522992672a8c5f937b410e8c05e194c81c729f715832c6e1303",
  "cid": "QmV1ee208ea41e17b522992672a8c5f937b410e8c05e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287290,
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
      "evaluated_at": 1760287290
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
  "sig": "256d430d733c8e92e14a6eaf0e73a8afbf3b1cc5adb2c24923eeee45f8d79c71"
}
```

Fraud detected: duplicate_transaction (score: 72)
Transaction: 111000029518652
Details: {'velocity': {'fraud_detected': True, 'risk_score': 60, 'details': {'transaction_count': 55, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 54, 'first_seen': 1760285763, 'matching_hash': 'e772ab4f6c2a0903'}}}een': 1760285763, 'matching_hash': '530c0ede13f83176'}}}