```json
{
  "id": "83c9330a41114584",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293712,
  "host_pid": "9e6742732c60:1",
  "hash": "ff12a46c698cb133e9fe6b0eb5ea9fce4f5afd9602d41aa49a0ded3e8069d1dc",
  "cid": "QmV1ff12a46c698cb133e9fe6b0eb5ea9fce4f5afd96",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293712,
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
      "evaluated_at": 1760293712
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
  "sig": "8f411e6f73ee87affd645c244e827116bf6899740ea626e812728362e690dbf1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105158691889
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 224, 'threshold': 50, 'total_amount': 62746880, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 223, 'first_seen': 1760285764, 'matching_hash': '7f09a9884a1a1f0e'}}}