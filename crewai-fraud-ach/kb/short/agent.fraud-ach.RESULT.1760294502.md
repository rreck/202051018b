```json
{
  "id": "605a1358efe46c93",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294502,
  "host_pid": "9e6742732c60:1",
  "hash": "f220071daaf7a344dbc55da07fe75e1a33fd20f9bccf0a73e967bbc4ae44a3bf",
  "cid": "QmV1f220071daaf7a344dbc55da07fe75e1a33fd20f9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294502,
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
      "evaluated_at": 1760294502
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
  "sig": "1b6a4ab28c015142627f01adb65bf84a8605b046f9cb72be56a2e65729345b54"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245017605
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 239, 'threshold': 50, 'total_amount': 112431814, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 238, 'first_seen': 1760285763, 'matching_hash': '04117a7715fe8402'}}}