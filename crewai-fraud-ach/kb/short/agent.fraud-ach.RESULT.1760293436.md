```json
{
  "id": "f9d05f32b757ed3a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293436,
  "host_pid": "9e6742732c60:1",
  "hash": "3f2699edae76b45e5ba9d4effb141018006d6bf3e61f9ffc39dcf7bb4152d71d",
  "cid": "QmV13f2699edae76b45e5ba9d4effb141018006d6bf3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293436,
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
      "evaluated_at": 1760293436
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
  "sig": "2db23bd2d43f58a28b2d2315b103e0442abbeb7c5e5c47a1ebaf7d3facaedaae"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029278927
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 218, 'threshold': 50, 'total_amount': 62996332, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 217, 'first_seen': 1760285765, 'matching_hash': '45338af8ff50831c'}}}