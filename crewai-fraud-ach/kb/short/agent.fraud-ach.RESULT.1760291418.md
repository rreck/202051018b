```json
{
  "id": "61068a3a59f333eb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291418,
  "host_pid": "9e6742732c60:1",
  "hash": "eb61018b431fa2333dfcb6fc9ad0a3524c356850be3da9d411912dd9091b8a77",
  "cid": "QmV1eb61018b431fa2333dfcb6fc9ad0a3524c356850",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291418,
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
      "evaluated_at": 1760291418
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
  "sig": "fde5e94e3d5bb758be767aec5a184e8e62269daf74a41249779721a3cad1cd05"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105158642736
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 174, 'threshold': 50, 'total_amount': 31866360, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 173, 'first_seen': 1760285765, 'matching_hash': '1f64147e0a165b3c'}}}