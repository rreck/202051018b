```json
{
  "id": "524e6962a386b82d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290353,
  "host_pid": "9e6742732c60:1",
  "hash": "e0cdc31622e1c1d66ec2aab6eb2dd5bbbb665cc783aa4ed681afe19c8f6d3d1b",
  "cid": "QmV1e0cdc31622e1c1d66ec2aab6eb2dd5bbbb665cc7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290353,
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
      "evaluated_at": 1760290353
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
  "sig": "26c98bd521c94c9f376ae00030a4834ff2db10663efb04aeac067da3f1faa0bd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000029354583
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 148, 'threshold': 50, 'total_amount': 11742024, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 147, 'first_seen': 1760285763, 'matching_hash': 'dbced9ae96be05e0'}}}