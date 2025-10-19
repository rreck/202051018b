```json
{
  "id": "084e06390b20fb5c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287307,
  "host_pid": "9e6742732c60:1",
  "hash": "9ef9a1f80ae9bdbc0cb2289b6c8fa12729dc1752b0a7c907ac230b227e4294f9",
  "cid": "QmV19ef9a1f80ae9bdbc0cb2289b6c8fa12729dc1752",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287307,
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
      "evaluated_at": 1760287307
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "a18acfaca1d127fd600af01c6177c07b4217c5b6fbb640bad1c6389cc0254b89"
}
```

Fraud detected: duplicate_transaction (score: 72)
Transaction: 021000029386599
Details: {'velocity': {'fraud_detected': True, 'risk_score': 60, 'details': {'transaction_count': 55, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 54, 'first_seen': 1760285765, 'matching_hash': 'b64c8fcbcd38380f'}}}