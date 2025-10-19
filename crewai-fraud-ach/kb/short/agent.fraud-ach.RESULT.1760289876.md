```json
{
  "id": "6ecb18659b79f179",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289876,
  "host_pid": "9e6742732c60:1",
  "hash": "32e5d56320c026d8a92a4534d6326faa6b3ac46c8c37b9843a335fdcc0fb281a",
  "cid": "QmV132e5d56320c026d8a92a4534d6326faa6b3ac46c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289876,
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
      "evaluated_at": 1760289876
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
  "sig": "2de3759bb7f67d0d47ec045866dc783a4087c162432e054eb44d39d5190a99ec"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009590866940
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 135, 'threshold': 50, 'total_amount': 57374460, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 134, 'first_seen': 1760285765, 'matching_hash': '66ff896a34603a53'}}}