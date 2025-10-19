```json
{
  "id": "b0c40a91d911dc70",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292561,
  "host_pid": "9e6742732c60:1",
  "hash": "9f538db75b2ea3471e9ca684664170ad0a5042dea168577e2a23e22bcea91bf4",
  "cid": "QmV19f538db75b2ea3471e9ca684664170ad0a5042de",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292561,
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
      "evaluated_at": 1760292561
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
  "sig": "727f86b01788e81f307183bb35b161dd6e1afef65e2e5bf42e5bd0cf62471fc3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009599696280
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 276, 'threshold': 50, 'total_amount': 65733540, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 275, 'first_seen': 1760284979, 'matching_hash': '32fd26aee1bbbffc'}}}