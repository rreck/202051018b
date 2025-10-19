```json
{
  "id": "1731eec68a474a85",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290953,
  "host_pid": "9e6742732c60:1",
  "hash": "70a4a72c782c01d69f51ad7d0d1e1ff5d2eefbea0ac2da2d4f75be818685df41",
  "cid": "QmV170a4a72c782c01d69f51ad7d0d1e1ff5d2eefbea",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290953,
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
      "evaluated_at": 1760290953
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
  "sig": "e85c81023fcf92903883d8f52ae98f815ac1cb1935257d208af6e595443c32c1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000021660412
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 163, 'threshold': 50, 'total_amount': 52513873, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 162, 'first_seen': 1760285764, 'matching_hash': '19be1dcf8b4c513c'}}}