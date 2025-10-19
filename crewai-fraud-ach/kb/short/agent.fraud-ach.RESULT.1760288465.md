```json
{
  "id": "234367e716b10a2f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288465,
  "host_pid": "9e6742732c60:1",
  "hash": "9e3141261996bc2218ac6d2b2dd330dffcb7efe4dce0878af490ef976e8fe22f",
  "cid": "QmV19e3141261996bc2218ac6d2b2dd330dffcb7efe4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288465,
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
      "evaluated_at": 1760288465
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
  "sig": "55f48e3a85cdb50b9990ed6eb8c74d86760546dab6bd28130a33e3e2ece4214c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000246112063
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 94, 'threshold': 50, 'total_amount': 13047012, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 93, 'first_seen': 1760285763, 'matching_hash': '58be5dc306b57ee9'}}}}}