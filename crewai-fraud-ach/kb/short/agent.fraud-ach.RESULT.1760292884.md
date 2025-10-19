```json
{
  "id": "14b5146cbca416b3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292884,
  "host_pid": "9e6742732c60:1",
  "hash": "7b67f7f114c83f688f09e2ce3bad4ca135b294cb54608e882d00b5cca5f0acbd",
  "cid": "QmV17b67f7f114c83f688f09e2ce3bad4ca135b294cb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292884,
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
      "evaluated_at": 1760292884
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
  "sig": "712b19df893fe6be87d63cc89ca3fc165d7357c51851eaf76daa6e2ed1d53aa7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591103574
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 207, 'threshold': 50, 'total_amount': 96829425, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 206, 'first_seen': 1760285763, 'matching_hash': 'b913753ac5280baa'}}}