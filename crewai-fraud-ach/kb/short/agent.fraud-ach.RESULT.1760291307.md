```json
{
  "id": "0a8afb5a05117e86",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291307,
  "host_pid": "9e6742732c60:1",
  "hash": "d776a2538574fe7378ccbd4fa04f6a48439e85c6685ffe664ecdd50f37c53f61",
  "cid": "QmV1d776a2538574fe7378ccbd4fa04f6a48439e85c6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291307,
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
      "evaluated_at": 1760291307
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
  "sig": "5004afdacce8fcd9d31fa6c41d44e00049ac2a4940c5b8e605939a39feecf2c5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469776996
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 172, 'threshold': 50, 'total_amount': 28259600, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 171, 'first_seen': 1760285763, 'matching_hash': '22919e1176d7109e'}}}