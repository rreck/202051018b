```json
{
  "id": "4de7c9f67ca1760e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293754,
  "host_pid": "9e6742732c60:1",
  "hash": "1759e91ba6eb32a42e2326b4a6a30bf4fc7db568696148bb89a8bc89b17ec760",
  "cid": "QmV11759e91ba6eb32a42e2326b4a6a30bf4fc7db568",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293754,
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
      "evaluated_at": 1760293754
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
  "sig": "a8965f3494eda9963d9c5ce45ab40aec547a7b6b7855b9f5a39ff9beac453138"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469479183
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 225, 'threshold': 50, 'total_amount': 30057750, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 224, 'first_seen': 1760285763, 'matching_hash': '2b83b0aed5f7590d'}}}