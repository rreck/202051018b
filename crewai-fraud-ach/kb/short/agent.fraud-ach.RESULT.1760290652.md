```json
{
  "id": "2ddc46a0676bfa4b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290652,
  "host_pid": "9e6742732c60:1",
  "hash": "d556677e0ec2073ef29861039a8f678f1612f87145b37e2e15e11c1c1b219970",
  "cid": "QmV1d556677e0ec2073ef29861039a8f678f1612f871",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290652,
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
      "evaluated_at": 1760290652
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
  "sig": "d801c86bc0560d9f06edac3b0e9e5ad3256f1e655e19417b6b7ef56e9eefce14"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598639172
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 156, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 155, 'first_seen': 1760285763, 'matching_hash': '9f277109cf79f7ea'}}}een': 1760285763, 'matching_hash': '38281b9a763b4bf2'}}}