```json
{
  "id": "8991aced99057235",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287956,
  "host_pid": "9e6742732c60:1",
  "hash": "bf6ec866a80e4da4ec45106519c4d7d847857a918aa575e447f63483efd8f146",
  "cid": "QmV1bf6ec866a80e4da4ec45106519c4d7d847857a91",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287956,
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
      "evaluated_at": 1760287956
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
  "sig": "9a294ddd111b5cd8599bf1028335fdc13c86ebb451f6b61cadfac062f0ab30d3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009599855850
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 78, 'threshold': 50, 'total_amount': 28204332, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 77, 'first_seen': 1760285763, 'matching_hash': 'c589ba109b80fe94'}}}