```json
{
  "id": "2b97014c0fe778fc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289015,
  "host_pid": "9e6742732c60:1",
  "hash": "eb6311e889125c14ee39045eaabdb07ac729f899aec0fd21f97aee93e2b6d404",
  "cid": "QmV1eb6311e889125c14ee39045eaabdb07ac729f899",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289015,
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
      "evaluated_at": 1760289015
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
  "sig": "f3856a3e5290272e3636b19733c032225dd2ca2ed51a05bf84ad3293bd622830"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201461315278
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 111, 'threshold': 50, 'total_amount': 26946138, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 110, 'first_seen': 1760285763, 'matching_hash': 'd87579b8c6b654cb'}}}