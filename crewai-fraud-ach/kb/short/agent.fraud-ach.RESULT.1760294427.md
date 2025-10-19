```json
{
  "id": "30f4efa0cc531dcb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294427,
  "host_pid": "9e6742732c60:1",
  "hash": "61ee87074eed0a8ab11b29c0cbd1f60a5e04f0b62ac89fd39dacae52375c02b7",
  "cid": "QmV161ee87074eed0a8ab11b29c0cbd1f60a5e04f0b6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294427,
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
      "evaluated_at": 1760294427
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
  "sig": "168d039db68a2b1bff9e44094e3683871ad8f7fc6b19213c8d7601ecf53be00a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460250809
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 238, 'threshold': 50, 'total_amount': 100202284, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 237, 'first_seen': 1760285763, 'matching_hash': 'b939c4c4097f2f1f'}}}nt_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}