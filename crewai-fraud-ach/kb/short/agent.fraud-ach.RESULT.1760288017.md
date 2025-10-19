```json
{
  "id": "45da74faead6a5bb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288017,
  "host_pid": "9e6742732c60:1",
  "hash": "8515c8d9797f23c0070dd45a4b90e94707996cd526794bcd2f84f08084f67c5b",
  "cid": "QmV18515c8d9797f23c0070dd45a4b90e94707996cd5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288017,
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
      "evaluated_at": 1760288017
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
  "sig": "44e3644ee82618e2498f4a830516749780ea29354e49df2bbcdc8d3ff8c72530"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100273476886
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 80, 'threshold': 50, 'total_amount': 24543600, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 79, 'first_seen': 1760285763, 'matching_hash': 'e52038f69d26fe5a'}}}aly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 7209366}}}