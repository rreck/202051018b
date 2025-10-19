```json
{
  "id": "7af5f975db64b302",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294505,
  "host_pid": "9e6742732c60:1",
  "hash": "bbcc91af4a09e659f5c4b239a1f9bd75b2c72ad49ab2e9520b82f9791cb23c3e",
  "cid": "QmV1bbcc91af4a09e659f5c4b239a1f9bd75b2c72ad4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294505,
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
      "evaluated_at": 1760294505
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
  "sig": "510d3e55936540ee656d2a9d61075958df700260ba3501c363b7dc7840ec620c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009599696280
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 315, 'threshold': 50, 'total_amount': 75021975, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 314, 'first_seen': 1760284979, 'matching_hash': '32fd26aee1bbbffc'}}}