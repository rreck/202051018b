```json
{
  "id": "7bed5ad316cb0c42",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286010,
  "host_pid": "9e6742732c60:1",
  "hash": "1441e837b99c763ce3210f2bdce3d82f9da91d791d23ceb993c0290e94dadb12",
  "cid": "QmV11441e837b99c763ce3210f2bdce3d82f9da91d79",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286010,
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
      "evaluated_at": 1760286010
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
  "sig": "f55bcb0d3377c869002969fe5ac82b67f18b226390f15ad914b6fe98c6f0740a"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000039498282
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 10, 'first_seen': 1760285765, 'matching_hash': 'dad018b424b66512'}}}