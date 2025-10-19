```json
{
  "id": "0687f1268b5219ce",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294178,
  "host_pid": "9e6742732c60:1",
  "hash": "2b9df70708332cecc030a83019fddcbbfe8fea49032752aa00a579ce8a567241",
  "cid": "QmV12b9df70708332cecc030a83019fddcbbfe8fea49",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294178,
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
      "evaluated_at": 1760294178
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
  "sig": "28bd68050c76654e21aad5e06d218b54cca35b128e39e947ac104747a27cda2d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105150369382
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 233, 'threshold': 50, 'total_amount': 83369264, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 232, 'first_seen': 1760285763, 'matching_hash': '1d04175be49b6deb'}}}