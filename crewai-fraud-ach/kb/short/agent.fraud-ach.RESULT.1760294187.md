```json
{
  "id": "5f1c7164d05115e0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294187,
  "host_pid": "9e6742732c60:1",
  "hash": "d5487aa05352f7ed336308cfa3ae79beb8b70d069c1fea614e25ece670b707a3",
  "cid": "QmV1d5487aa05352f7ed336308cfa3ae79beb8b70d06",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294187,
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
      "evaluated_at": 1760294187
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
  "sig": "711b01d5973b1808d8e9ebadd8cdfb85007befb8cdeebc8a0adfde13829ef15c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464346208
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 233, 'threshold': 50, 'total_amount': 23300000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 232, 'first_seen': 1760285763, 'matching_hash': 'be0548ed0e4f6107'}}}