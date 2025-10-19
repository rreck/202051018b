```json
{
  "id": "fc6a573e9867f4b8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291714,
  "host_pid": "9e6742732c60:1",
  "hash": "169985f5a201cde72b6a5b53d66d6b2da80577284a61eacd736ead60156eb04c",
  "cid": "QmV1169985f5a201cde72b6a5b53d66d6b2da8057728",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291714,
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
      "evaluated_at": 1760291714
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
  "sig": "f9ceab1aa9393037e2b0b0e3a6c05d1ece1842594bca6a80af62307b090638bb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000246289995
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 181, 'threshold': 50, 'total_amount': 18952872, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 180, 'first_seen': 1760285764, 'matching_hash': '1ab4d10c626d0dd7'}}}