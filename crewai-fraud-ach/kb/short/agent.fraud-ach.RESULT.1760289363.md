```json
{
  "id": "580fb8b090b257f4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289363,
  "host_pid": "9e6742732c60:1",
  "hash": "b70c5697ebdfd4d736be38acfbd12420c421d083998dd5feeebb53b0222bc89b",
  "cid": "QmV1b70c5697ebdfd4d736be38acfbd12420c421d083",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289363,
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
      "evaluated_at": 1760289363
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
  "sig": "cc1603fac8167eb7122ced2d2101d11b70d6165a9e5ef70b19623a56a5e3995d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465124688
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 121, 'threshold': 50, 'total_amount': 19910913, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 120, 'first_seen': 1760285763, 'matching_hash': 'c4099eb9aeb13a11'}}}