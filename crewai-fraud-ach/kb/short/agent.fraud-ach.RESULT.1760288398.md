```json
{
  "id": "ef41351f3f7fa827",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288398,
  "host_pid": "9e6742732c60:1",
  "hash": "d280064954c01818296c349b1dc2e5e02fb443afa66dbdf87fa2c53942d36aa2",
  "cid": "QmV1d280064954c01818296c349b1dc2e5e02fb443af",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288398,
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
      "evaluated_at": 1760288398
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
  "sig": "a8d05a4da55910d7fa21746d86a851e77675b88c6754572ffd71216d67b249f2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460216158
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 168, 'threshold': 50, 'total_amount': 44361744, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 167, 'first_seen': 1760284979, 'matching_hash': 'd03ac62e4cd65436'}}}