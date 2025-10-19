```json
{
  "id": "1e907305c18717ca",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289395,
  "host_pid": "9e6742732c60:1",
  "hash": "bcfdf961fc40fca964444c88d60b74ce0bcba7005607cf16a9bf36945ac7d6b4",
  "cid": "QmV1bcfdf961fc40fca964444c88d60b74ce0bcba700",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289395,
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
      "evaluated_at": 1760289395
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
  "sig": "0278f60c20dfeb14b2b417b6c249c87961473e6a77e72ef614f055ad6f5c026d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000240263900
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 122, 'threshold': 50, 'total_amount': 30500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 121, 'first_seen': 1760285764, 'matching_hash': 'e5d68d31887f65d4'}}}