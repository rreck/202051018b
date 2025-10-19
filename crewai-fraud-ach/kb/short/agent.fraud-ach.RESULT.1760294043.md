```json
{
  "id": "fc045e80df162691",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294043,
  "host_pid": "9e6742732c60:1",
  "hash": "c793ba1c27308b69f783b17adf03a5c5df26ddf3256583f48f262789f69a3aff",
  "cid": "QmV1c793ba1c27308b69f783b17adf03a5c5df26ddf3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294043,
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
      "evaluated_at": 1760294043
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
  "sig": "7292b4a54acf8a85ebd579681a90840a8fe28c775a10939668bb2d3d9f7580f4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274395247
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 230, 'threshold': 50, 'total_amount': 75406650, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 229, 'first_seen': 1760285765, 'matching_hash': '7ef610f7539e9ec6'}}}