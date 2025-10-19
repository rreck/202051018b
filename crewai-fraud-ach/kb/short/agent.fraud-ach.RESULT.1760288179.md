```json
{
  "id": "a17a0f3d96ed3aeb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288179,
  "host_pid": "9e6742732c60:1",
  "hash": "cffccfade6651a5ed8aab9c6458a07cd74dea35c03bd9ec191ff8a2b3a56898d",
  "cid": "QmV1cffccfade6651a5ed8aab9c6458a07cd74dea35c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288179,
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
      "evaluated_at": 1760288179
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
  "sig": "9a5d6025cdf413d3fd593d370d5a459d2d6e05d75c8596c05ab203bc4254c834"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000027165618
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 85, 'threshold': 50, 'total_amount': 22218405, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 84, 'first_seen': 1760285763, 'matching_hash': '01e7bf5fcf2bbeec'}}}