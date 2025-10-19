```json
{
  "id": "8091180d99d9b106",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292482,
  "host_pid": "9e6742732c60:1",
  "hash": "e3a53e362e90c8334a6d48511b4ba26cb4857b591a2bbe380b371fec50895672",
  "cid": "QmV1e3a53e362e90c8334a6d48511b4ba26cb4857b59",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292482,
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
      "evaluated_at": 1760292482
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
  "sig": "22ba8fe55e690cc7f8884c625ab695eb10a6e931b442675312f63f454457dd95"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000025001530
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 198, 'threshold': 50, 'total_amount': 47807892, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 197, 'first_seen': 1760285765, 'matching_hash': 'c7ad70870577ca51'}}}