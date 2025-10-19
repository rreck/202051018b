```json
{
  "id": "0d3866f294a9967f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290906,
  "host_pid": "9e6742732c60:1",
  "hash": "0d6c42a3887e13e1e07f703e6fd7c6900dc791db403be64e4ee6b8473bb8f19c",
  "cid": "QmV10d6c42a3887e13e1e07f703e6fd7c6900dc791db",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290906,
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
      "evaluated_at": 1760290906
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
  "sig": "6fbe8d1098f50cc75855cbe67cec886ed186e6d98b1f7906b514d06ab527824c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009590785424
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 162, 'threshold': 50, 'total_amount': 10974366, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 161, 'first_seen': 1760285763, 'matching_hash': 'b02577e012abfee0'}}}