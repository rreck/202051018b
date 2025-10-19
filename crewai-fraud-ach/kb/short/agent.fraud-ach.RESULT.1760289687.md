```json
{
  "id": "a7a214271d01576f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289687,
  "host_pid": "9e6742732c60:1",
  "hash": "9ca7d6a8ee95b390377566301a9d05b110074cfc4b767239afc41bbfe561e648",
  "cid": "QmV19ca7d6a8ee95b390377566301a9d05b110074cfc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289687,
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
      "evaluated_at": 1760289687
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
  "sig": "34f7a3e24231b5e13006e09285df825ea6dd8baa79a157025090015300ed2cb3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154887163
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 206, 'threshold': 50, 'total_amount': 72470594, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 205, 'first_seen': 1760284979, 'matching_hash': '445784114b53d57b'}}}