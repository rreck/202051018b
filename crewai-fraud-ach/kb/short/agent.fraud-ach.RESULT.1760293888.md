```json
{
  "id": "012c35d0cf5b9577",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293888,
  "host_pid": "9e6742732c60:1",
  "hash": "1ee22e8faa97b0b00d2d02cad55ee09505a869436126227ce38c503411e84264",
  "cid": "QmV11ee22e8faa97b0b00d2d02cad55ee09505a86943",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293888,
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
      "evaluated_at": 1760293888
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
  "sig": "c3c47ac85cd36f082f7fc7c9f4614c519a1489bd7419dd6c396c0b7ad8a77db8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201467961793
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 227, 'threshold': 50, 'total_amount': 15210589, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 226, 'first_seen': 1760285765, 'matching_hash': '7ef856857e97207f'}}}