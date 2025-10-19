```json
{
  "id": "663b19facacadec2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289264,
  "host_pid": "9e6742732c60:1",
  "hash": "383161e6327481d7fbbeb45a3696b3b1278a00741556c5191b953f6060337f47",
  "cid": "QmV1383161e6327481d7fbbeb45a3696b3b1278a0074",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289264,
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
      "evaluated_at": 1760289264
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
  "sig": "70a68d2bd93bf01f68a236f44567b3e4d197895727590e8f0ed93f24116d7beb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000027229959
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 118, 'threshold': 50, 'total_amount': 51249170, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 117, 'first_seen': 1760285763, 'matching_hash': 'f31e697a4f515fbb'}}}