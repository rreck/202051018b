```json
{
  "id": "a7ea516d0485bf16",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294881,
  "host_pid": "9e6742732c60:1",
  "hash": "be0266325dc740ce4448d5ac7c12d3f15e5fbd1379e859ecc1941821aa356df3",
  "cid": "QmV1be0266325dc740ce4448d5ac7c12d3f15e5fbd13",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294881,
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
      "evaluated_at": 1760294881
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
  "sig": "41d973db6c07b37071c491d75d64050d7486495ef5f9275cc3aeed9a2d54ea21"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000031758687
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 246, 'threshold': 50, 'total_amount': 99327912, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 245, 'first_seen': 1760285763, 'matching_hash': '8a33e153fff23185'}}}