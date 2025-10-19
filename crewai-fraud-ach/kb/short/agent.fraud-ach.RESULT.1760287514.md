```json
{
  "id": "53c78aad0639ed62",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287514,
  "host_pid": "9e6742732c60:1",
  "hash": "7967d6c110ffd599af5c8b7c1275b16cd04a6fdb1b4e8024e6c0c3f354c649e0",
  "cid": "QmV17967d6c110ffd599af5c8b7c1275b16cd04a6fdb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287514,
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
      "evaluated_at": 1760287514
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
  "sig": "5073017a487057dcf8c1650b17d30f52569e3045f5c49aa48cabf6b381d754d2"
}
```

Fraud detected: duplicate_transaction (score: 80)
Transaction: 026009591278492
Details: {'velocity': {'fraud_detected': True, 'risk_score': 76, 'details': {'transaction_count': 63, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 62, 'first_seen': 1760285763, 'matching_hash': '3e8e4f28808ab222'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '561028991', 'validation_error': 'Invalid routing number checksum'}}}'validation_error': 'Invalid routing number checksum'}}}