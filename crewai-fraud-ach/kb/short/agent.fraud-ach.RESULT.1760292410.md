```json
{
  "id": "12fd183aa70a5c89",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292410,
  "host_pid": "9e6742732c60:1",
  "hash": "fd7e1da528c31da01ecf3a2483ff5d4cf5b4c7a5f86100f2b84f4d934e12b38d",
  "cid": "QmV1fd7e1da528c31da01ecf3a2483ff5d4cf5b4c7a5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292410,
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
      "evaluated_at": 1760292410
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
  "sig": "9a849953e2e0300d810c0636b4fbaa984f17c250a26c1f13cef2f26066e150a7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025319716
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 197, 'threshold': 50, 'total_amount': 50375067, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 196, 'first_seen': 1760285764, 'matching_hash': '46cae66c8ff70b91'}}}