```json
{
  "id": "151f4dfd4597efe2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290394,
  "host_pid": "9e6742732c60:1",
  "hash": "cc6878367e2e50cb12e84a382ecf0d84c3d0a11d510326ed782a43ea7ac02a34",
  "cid": "QmV1cc6878367e2e50cb12e84a382ecf0d84c3d0a11d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290394,
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
      "evaluated_at": 1760290394
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
  "sig": "3a12f2e6fa629497e77cf12319d72eaa4673d620b8dcba79056ff210f05e9cfc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105152729668
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 149, 'threshold': 50, 'total_amount': 20896654, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 148, 'first_seen': 1760285763, 'matching_hash': 'e33e77be4df2721a'}}}