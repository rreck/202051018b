```json
{
  "id": "9b78ba8b89557047",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293923,
  "host_pid": "9e6742732c60:1",
  "hash": "940201152ebdce431b25e60a63854946a32813ea04b4c4f7eb95ae7a7b9ab198",
  "cid": "QmV1940201152ebdce431b25e60a63854946a32813ea",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293923,
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
      "evaluated_at": 1760293923
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
  "sig": "7fa47d1b15031df7ecb65ae1f39be273389297b37475fc18ce95b3a126be7fd4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000027541214
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 228, 'threshold': 50, 'total_amount': 11400000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 227, 'first_seen': 1760285764, 'matching_hash': 'af0421d8ed92230e'}}}