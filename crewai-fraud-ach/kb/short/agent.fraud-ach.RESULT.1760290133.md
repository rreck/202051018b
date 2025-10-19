```json
{
  "id": "41313b6f11725f23",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290133,
  "host_pid": "9e6742732c60:1",
  "hash": "c85d9db8888e9e75778b5ca9fecea680485b8663cbb6614bfb5cea8956533bca",
  "cid": "QmV1c85d9db8888e9e75778b5ca9fecea680485b8663",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290133,
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
      "evaluated_at": 1760290133
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
  "sig": "bad8fd0bfbc78a370c18cc0a0382e9fd981c9aae19d0320e0690c6d9180e76f5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241271841
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 142, 'threshold': 50, 'total_amount': 61339882, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 141, 'first_seen': 1760285764, 'matching_hash': '100dee2bbeee5c05'}}}