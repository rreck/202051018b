```json
{
  "id": "b934197f2ef612c3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290788,
  "host_pid": "9e6742732c60:1",
  "hash": "ffa0d0fc5fd785cf96f5fcebb539f865f35bb82f985736eb06751a0c347754c2",
  "cid": "QmV1ffa0d0fc5fd785cf96f5fcebb539f865f35bb82f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290788,
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
      "evaluated_at": 1760290788
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
  "sig": "8aabc14bb1de2cfbcd80bd8ab76855b169beb25a18ace2759a3588641fd427e6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100273334011
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 159, 'threshold': 50, 'total_amount': 16520736, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 158, 'first_seen': 1760285763, 'matching_hash': 'fc8e9fbdacff3816'}}}