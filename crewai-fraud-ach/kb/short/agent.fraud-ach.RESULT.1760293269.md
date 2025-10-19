```json
{
  "id": "e0b6fd0c7fdfc122",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293269,
  "host_pid": "9e6742732c60:1",
  "hash": "183549de9a1d4e4fa824222f33bc7529a36914c83fd7b759944578a5f8e96a6d",
  "cid": "QmV1183549de9a1d4e4fa824222f33bc7529a36914c8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293269,
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
      "evaluated_at": 1760293269
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
  "sig": "5b33e50f5b4147ccb63f2ee9722c3d3a34f2720ad49f32853e35205dc4b362d5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469045536
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 215, 'threshold': 50, 'total_amount': 73712535, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 214, 'first_seen': 1760285763, 'matching_hash': 'd92613c41315e1ec'}}}