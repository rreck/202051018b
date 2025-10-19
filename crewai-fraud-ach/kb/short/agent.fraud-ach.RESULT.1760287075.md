```json
{
  "id": "85c72f8371436668",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287075,
  "host_pid": "9e6742732c60:1",
  "hash": "6e7c496d18332787aab1d0bb0adf0806dcd6230d0acbdfc9b37437b420e87855",
  "cid": "QmV16e7c496d18332787aab1d0bb0adf0806dcd6230d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287075,
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
      "evaluated_at": 1760287075
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
  "sig": "01e1bec327785cdb34b039f1a7915c1479d7a875eddb26c64a8affd0d96f5388"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000036177444
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 46, 'first_seen': 1760285764, 'matching_hash': '11850a408d1201a4'}}}