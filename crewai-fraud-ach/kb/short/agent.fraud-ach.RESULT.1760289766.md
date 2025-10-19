```json
{
  "id": "9329ae54a8909af3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289766,
  "host_pid": "9e6742732c60:1",
  "hash": "9aaee00c170a1785ed111a56035faba9083ce14ff7afb7554aba2601e487b740",
  "cid": "QmV19aaee00c170a1785ed111a56035faba9083ce14f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289766,
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
      "evaluated_at": 1760289766
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
  "sig": "283781a0f7703b872ab8dd3d293ec39a24fa9ca57e94eae1a257b4a6d2adf7ea"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244752813
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 132, 'threshold': 50, 'total_amount': 19409412, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 131, 'first_seen': 1760285765, 'matching_hash': 'eddee7b4753d10e9'}}}