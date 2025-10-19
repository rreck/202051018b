```json
{
  "id": "02896635b1c2ae35",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293140,
  "host_pid": "9e6742732c60:1",
  "hash": "3bd14ee49f84d020c007bb8c63042e072e0f081978f2e44dce7a35fdd2c0dd2e",
  "cid": "QmV13bd14ee49f84d020c007bb8c63042e072e0f0819",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293140,
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
      "evaluated_at": 1760293140
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
  "sig": "938d34b51dfd10f4d37ff51f2949ba6057bf57cbea0abfaa3d6f9f48ab3e986f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244947778
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 212, 'threshold': 50, 'total_amount': 62918420, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 211, 'first_seen': 1760285763, 'matching_hash': '9c8f06e6a18eec99'}}}