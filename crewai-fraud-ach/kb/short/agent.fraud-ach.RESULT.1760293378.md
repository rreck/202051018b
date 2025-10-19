```json
{
  "id": "d3c4fe4feaa34830",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293378,
  "host_pid": "9e6742732c60:1",
  "hash": "553262b0f429ff0432528cb269b0b61681d94819d0d97c4aee24f78167ed679b",
  "cid": "QmV1553262b0f429ff0432528cb269b0b61681d94819",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293378,
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
      "evaluated_at": 1760293378
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
  "sig": "c03b16ddaccc4c7fd4aea466ee1ae780515a03a5f333c1e550ac1dc7b924e67f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000023553215
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 217, 'threshold': 50, 'total_amount': 84976983, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 216, 'first_seen': 1760285763, 'matching_hash': '85da211728f5a38f'}}}