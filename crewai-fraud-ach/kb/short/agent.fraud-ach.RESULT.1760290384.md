```json
{
  "id": "e90aad7de74227ec",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290384,
  "host_pid": "9e6742732c60:1",
  "hash": "ca471f15843c1bb262012d60bcf1d68d64ac430045be0c26f75bc8602d0dcc3b",
  "cid": "QmV1ca471f15843c1bb262012d60bcf1d68d64ac4300",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290384,
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
      "evaluated_at": 1760290384
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
  "sig": "ca0f53ddf3d505b3f5c3425199050db07e449540f6fab653d01d0323c7cd9e0e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244433200
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 149, 'threshold': 50, 'total_amount': 22159876, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 148, 'first_seen': 1760285763, 'matching_hash': 'e1a08016c5f05bd5'}}}