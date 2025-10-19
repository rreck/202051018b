```json
{
  "id": "00b6472251582612",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291152,
  "host_pid": "9e6742732c60:1",
  "hash": "1ca2ba7676ada88aafda9843fd298edd07c3e16f8f1472482523abdb7d486908",
  "cid": "QmV11ca2ba7676ada88aafda9843fd298edd07c3e16f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291152,
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
      "evaluated_at": 1760291152
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "amount_anomaly",
    "risk_critical"
  ],
  "sig": "e83e08c154c5119c16d8290d901155a762392e5fa89c026d149b2acfc196499d"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 111000021698868
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 244, 'threshold': 50, 'total_amount': 1381780540, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 243, 'first_seen': 1760284979, 'matching_hash': '4224f1af7034834c'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 5663035}}}_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 6481360}}}