```json
{
  "id": "0b88bf99d01a476e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291065,
  "host_pid": "9e6742732c60:1",
  "hash": "c9eb67a32de8699d40e0d0858cbbaedbedc614a5f97a4b90ed2cc99ede29f44f",
  "cid": "QmV1c9eb67a32de8699d40e0d0858cbbaedbedc614a5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291065,
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
      "evaluated_at": 1760291065
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
  "sig": "4de0edfa65784465979a2524d227bcf437ef60d56e64db0afd5581a5a406ee21"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105152772165
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 166, 'threshold': 50, 'total_amount': 48240596, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 165, 'first_seen': 1760285764, 'matching_hash': '9371db7725d4e0a9'}}}