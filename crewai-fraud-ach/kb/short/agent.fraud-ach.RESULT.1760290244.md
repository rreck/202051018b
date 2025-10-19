```json
{
  "id": "59cb137d42a7ad5e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290244,
  "host_pid": "9e6742732c60:1",
  "hash": "4f345407775fb1177512f522552180b64ad145ec0040b0821b381412f90c166c",
  "cid": "QmV14f345407775fb1177512f522552180b64ad145ec",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290244,
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
      "evaluated_at": 1760290244
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
  "sig": "7d9afca448c7b9ca9efa02ea809af66560856da135c5dc2d0c9110339764688a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154440687
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 145, 'threshold': 50, 'total_amount': 40630595, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 144, 'first_seen': 1760285763, 'matching_hash': '04c13f034fff9f4d'}}}