```json
{
  "id": "15d825bf9c99ffbe",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294204,
  "host_pid": "9e6742732c60:1",
  "hash": "34a4f3891262623530d677e91ad7973311d4dea20994f1c7a69cc3250b94ec7a",
  "cid": "QmV134a4f3891262623530d677e91ad7973311d4dea2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294204,
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
      "evaluated_at": 1760294204
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
  "sig": "c8c2a37175191c67e0c07e258446b2f3a239411d9116cc5e044f15260cc867b6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 233, 'threshold': 50, 'total_amount': 74151784, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 232, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}